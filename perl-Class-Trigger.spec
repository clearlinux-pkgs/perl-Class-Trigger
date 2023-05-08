#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Trigger
Version  : 0.15
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Class-Trigger-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Class-Trigger-0.15.tar.gz
Summary  : 'Mixin to add / call inheritable triggers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Trigger-license = %{version}-%{release}
Requires: perl-Class-Trigger-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::Scalar)
BuildRequires : perl(IO::WrapTie)

%description
NAME
Class::Trigger - Mixin to add / call inheritable triggers
SYNOPSIS
package Foo;
use Class::Trigger;

sub foo {
my $self = shift;
$self->call_trigger('before_foo');
# some code ...
$self->call_trigger('middle_of_foo');
# some code ...
$self->call_trigger('after_foo');
}

package main;
Foo->add_trigger(before_foo => \&sub1);
Foo->add_trigger(after_foo => \&sub2);

my $foo = Foo->new;
$foo->foo;            # then sub1, sub2 called

# triggers are inheritable
package Bar;
use base qw(Foo);

Bar->add_trigger(before_foo => \&sub);

# triggers can be object based
$foo->add_trigger(after_foo => \&sub3);
$foo->foo;            # sub3 would appply only to this object

%package dev
Summary: dev components for the perl-Class-Trigger package.
Group: Development
Provides: perl-Class-Trigger-devel = %{version}-%{release}
Requires: perl-Class-Trigger = %{version}-%{release}

%description dev
dev components for the perl-Class-Trigger package.


%package license
Summary: license components for the perl-Class-Trigger package.
Group: Default

%description license
license components for the perl-Class-Trigger package.


%package perl
Summary: perl components for the perl-Class-Trigger package.
Group: Default
Requires: perl-Class-Trigger = %{version}-%{release}

%description perl
perl components for the perl-Class-Trigger package.


%prep
%setup -q -n Class-Trigger-0.15
cd %{_builddir}/Class-Trigger-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Trigger
cp %{_builddir}/Class-Trigger-0.15/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Trigger/d9d9a4124d4fbb52604682345fe32ae800ec92fd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Trigger.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Trigger/d9d9a4124d4fbb52604682345fe32ae800ec92fd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
