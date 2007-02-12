%define _name Mail
Summary:	ROX-Mail provides mail/no mail notification by its icon
Summary(pl.UTF-8):   ROX-Mail, poprzez swoją ikonę, powiadamia o nowej poczcie
Name:		rox-%{_name}
Version:	0.3.7
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	3c9959ecdfc4bdd8569d8cd5f3a0d786
Patch0:		%{name}-mailers.patch
URL:		http://www.kerofin.demon.co.uk/rox/mail.html
Requires:	/bin/mail
Requires:	python-pygtk-gtk
Requires:	python-PyXML
%pyrequires_eq	python
Requires:	rox >= 2.3
Requires:	rox-Lib2 >= 1.9.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Mail an applet which indicates whether or not you have new mail.
You can also use it to launch your favourite mail client.

%description -l pl.UTF-8
ROX-Mail jest apletem sprawdzającym czy masz nowe wiadomości pocztowe.
Możesz także używać tego apletu aby uruchomić swojego ulubionego
klienta pocztowego.

%prep
%setup -q -n %{_name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,pixmaps}

install .DirIcon App* *.py Options.xml $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install pixmaps/*.xpm $RPM_BUILD_ROOT%{_roxdir}/%{_name}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %{_roxdir}/%{_name}/*Run
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/*.py
%{_roxdir}/%{_name}/Help
%{_roxdir}/%{_name}/pixmaps
%dir %{_roxdir}/%{_name}
