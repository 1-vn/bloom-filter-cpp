{
  "targets": [{
    "target_name": "sample",
    "type": "executable",
    "sources": [
      "main.cpp",
      "BloomFilter.cpp",
      "BloomFilter.h"
    ],
    "include_dirs": [
      ".",
    ],
    "conditions": [
      ['OS=="win"', {
        }, {
          'cflags_cc': [ '-fexceptions' ]
        }
      ]
    ],
    "xcode_settings": {
      "OTHER_CFLAGS": [ "-ObjC" ],
      "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11","-stdlib=libc++", "-v"],
      "OTHER_LDFLAGS": ["-stdlib=libc++"],
      "MACOSX_DEPLOYMENT_TARGET": "10.9",
      "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
    },
  }, {
    "target_name": "test",
    "type": "executable",
    "sources": [
      "./test/test-main.cpp",
      "./test/test-bloom.cpp",
      "./test/util.cpp",
      "BloomFilter.cpp",
    ],
    "include_dirs": [
      ".",
      "<!(node -e \"require('cppunitlite')\")",
      "<!(node -e \"require('nan')\")"
    ],
    "dependencies": [
      "node_modules/cppunitlite/binding.gyp:CppUnitLite",
    ],
    "conditions": [
      ['OS=="win"', {
        }, {
          'cflags_cc': [ '-fexceptions' ]
        }
      ]
    ],
    "xcode_settings": {
      "OTHER_CFLAGS": [ "-ObjC" ],
      "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11","-stdlib=libc++", "-v"],
      "OTHER_LDFLAGS": ["-stdlib=libc++"],
      "MACOSX_DEPLOYMENT_TARGET": "10.9",
      "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
    },
  }]
}
