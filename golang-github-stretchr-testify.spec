#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-stretchr-testify
Version  : c5d7a69bf8a2c9c374798160849c071093e41dd1
Release  : 9
URL      : https://github.com/stretchr/testify/archive/c5d7a69bf8a2c9c374798160849c071093e41dd1.tar.gz
Source0  : https://github.com/stretchr/testify/archive/c5d7a69bf8a2c9c374798160849c071093e41dd1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause HPND MIT
BuildRequires : go

%description
This directory tree is generated automatically by godep.
Please do not edit.
See https://github.com/tools/godep for more information.

%prep
%setup -q -n testify-c5d7a69bf8a2c9c374798160849c071093e41dd1

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/stretchr/testify"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/stretchr/testify

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/stretchr/testify/_codegen/main.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/assertion_forward.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/errors.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/forward_assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/forward_assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/http_assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/http_assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/http/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/http/test_response_writer.go
/usr/lib/golang/src/github.com/stretchr/testify/http/test_round_tripper.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/mock.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/mock_test.go
/usr/lib/golang/src/github.com/stretchr/testify/package_test.go
/usr/lib/golang/src/github.com/stretchr/testify/require/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/require/forward_requirements.go
/usr/lib/golang/src/github.com/stretchr/testify/require/forward_requirements_test.go
/usr/lib/golang/src/github.com/stretchr/testify/require/require.go
/usr/lib/golang/src/github.com/stretchr/testify/require/require_forward.go
/usr/lib/golang/src/github.com/stretchr/testify/require/requirements.go
/usr/lib/golang/src/github.com/stretchr/testify/require/requirements_test.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/interfaces.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/suite.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/suite_test.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/bypass.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/bypasssafe.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/common.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/config.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/dump.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/format.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/davecgh/go-spew/spew/spew.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/pmezard/go-difflib/difflib/difflib.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/accessors.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/constants.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/conversions.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/map.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/mutations.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/security.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/tests.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/type_specific_codegen.go
/usr/lib/golang/src/github.com/stretchr/testify/vendor/github.com/stretchr/objx/value.go
