INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_OWC owc)

FIND_PATH(
    OWC_INCLUDE_DIRS
    NAMES owc/api.h
    HINTS $ENV{OWC_DIR}/include
        ${PC_OWC_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    OWC_LIBRARIES
    NAMES gnuradio-owc
    HINTS $ENV{OWC_DIR}/lib
        ${PC_OWC_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/owcTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(OWC DEFAULT_MSG OWC_LIBRARIES OWC_INCLUDE_DIRS)
MARK_AS_ADVANCED(OWC_LIBRARIES OWC_INCLUDE_DIRS)
