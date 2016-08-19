RGB_INCDIR=matrix/include
RGB_LIBDIR=matrix/lib
RGB_LIBRARY_NAME=rgbmatrix
RGB_LIBRARY=$(RGB_LIBDIR)/lib$(RGB_LIBRARY_NAME).a
LDFLAGS+=-L$(RGB_LIBDIR) -l$(RGB_LIBRARY_NAME) -lrt -lm -lpthread

matrix-server : $(OBJECTS) $(RGB_LIBRARY)
  $(CXX) $(CXXFLAGS) $(OBJECTS) -o $@ $(LDFLAGS)