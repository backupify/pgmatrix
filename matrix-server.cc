#include <unistd.h>
#include <iostream>
#include <time.h>
#include <cstdio>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

#include "led-matrix.h"
#include "transformer.h"
#include "graphics.h"

#define PIPE_NAME "/tmp/pgmatrix"
#define PANEL_SIZE 32

class MatrixServer {
  public:
    MatrixServer(uint32_t b, uint32_t w, uint32_t h)
      : rows_(PANEL_SIZE), chain_(w * h), parallel_(1), width_(w * PANEL_SIZE), height_(h * PANEL_SIZE) {
      if (!io_.Init()) throw "GPIO Error";
      matrix_ = new rgb_matrix::RGBMatrix(&io_, rows_, chain_, parallel_);
      matrix_->set_luminance_correct(true);
      matrix_->SetBrightness(b);
      matrix_->SetPWMBits(8);
      transformer_ = new rgb_matrix::LinkedTransformer();
      matrix_->SetTransformer(transformer_);
      buffer_ = matrix_->CreateFrameCanvas();
      frameBuffer_ = new char[width_ * height_ * 3];
    }

    ~MatrixServer() {
      delete matrix_;
      transformer_->DeleteTransformers();
      delete transformer_;
    }

    void setBrightness(unsigned b) {
      matrix_->SetBrightness(b);
    }

    void setPixel(uint32_t x, uint32_t y, uint8_t r, uint8_t g, uint8_t b) {
      matrix_->SetPixel(x, y, r, g, b);
    }

    void setPixelBuffered(uint32_t x, uint32_t y, uint8_t r, uint8_t g, uint8_t b) {
      matrix_->transformer()->Transform(buffer_)->SetPixel(x, y, r, g, b);
    }

    void drawBuffer() {
      buffer_ = matrix_->SwapOnVSync(buffer_);
    }

    rgb_matrix::RGBMatrix& canvas() {
      return *matrix_;
    }

    void readFrame(FILE* file) {
      uint32_t bytes = width_ * height_ * 3;
      uint32_t bytes_read = 0;

      while (bytes_read < bytes) {
        int32_t b = fread(frameBuffer_ + bytes_read, 1, bytes - bytes_read, file);
        // if (b != 0)
        //   std::cout << "bytes: " << bytes  << " read: " << b << " from: " << file  << " errno: " << strerror(errno) << std::endl;
        bytes_read += b;
      }

      for (uint32_t x = 0; x < width_; ++x) {
        for (uint32_t y = 0; y < height_; ++y) {
          uint64_t pos = ((y * width_) + x) * 3;
          uint32_t x_0 = x, y_0 = y % PANEL_SIZE, row = y / PANEL_SIZE;
          x_0 = x_0 + row * width_;
          if (row % 2) {
            y_0 = (PANEL_SIZE - 1) - y_0;
            x_0 = width_ - (x_0 - ((width_) * row)) + (width_ - 1) * row;
          }
          setPixelBuffered(x_0, y_0, frameBuffer_[pos], frameBuffer_[pos + 1], frameBuffer_[pos + 2]);
        }
      }
      drawBuffer();
    }

  private:
    rgb_matrix::GPIO io_;
    rgb_matrix::RGBMatrix* matrix_;
    rgb_matrix::FrameCanvas* buffer_;
    rgb_matrix::LinkedTransformer* transformer_;
    uint32_t rows_, chain_, parallel_;
    uint32_t width_, height_;
    timespec time_;
    char* frameBuffer_;
};

int main(int argc, char* argv[]) {
  if (argc != 4) {
    std::cerr << "Invalid params. Usage:\n\tmatrix-server <brightness(0..100)> <width(1..32)> <height(1..32)>\n";
    exit(1);
  }
  uint8_t b = atoi(argv[1]);
  uint8_t w = atoi(argv[2]);
  uint8_t h = atoi(argv[3]);
  MatrixServer canvasInterface(b, w, h);
  int fd = open(PIPE_NAME, O_RDONLY);
  FILE* file = fdopen(fd, "r");

  while (true) {
    canvasInterface.readFrame(file);
    // usleep(3*1000);
  }

}