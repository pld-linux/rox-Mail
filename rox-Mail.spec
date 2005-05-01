%define _name Mail
Summary:	ROX-Mail provides mail/no mail notification by its icon
Summary(pl):	ROX-Mail, poprzez swoj� ikon�, powiadamia o nowej poczcie
Name:		rox-%{_name}
Version:	0.3.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	3c9959ecdfc4bdd8569d8cd5f3a0d786
URL:		http://www.kerofin.demon.co.uk/rox/mail.html
Requires:	python-pygtk-gtk
Requires:	python-PyXML
%pyrequires_eq	python
Requires:	rox >= 2.2.0-2
Requires:	rox-Lib2 >= 1.9.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Mail an applet which indicates whether or not you have new mail.
You can also use it to launch your favourite mail client.

%description -l pl
ROX-Mail jest apletem sprawdzaj�cym czy masz nowe wiadomo�ci pocztowe.
Mo�esz tak�e u�ywa� tego apletu aby uruchomi� swojego ulubionego
klienta pocztowego.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,pixmaps}

install .DirIcon App* *.py Options.xml $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install pixmaps/*.xpm $RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %{_appsdir}/%{_name}/*Run
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/*.py
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/pixmaps
%dir %{_appsdir}/%{_name}
