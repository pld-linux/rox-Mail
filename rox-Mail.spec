%define _name Mail
Summary:	ROX-Mail provides mail/no mail notification by its icon
Summary(pl):	ROX-Mail, poprzez swoj± ikonê, powiadamia o nowej poczcie
Name:		rox-%{_name}
Version:	0.1.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#mail
Requires:	python-pygtk-gtk
Requires:	python-PyXML
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Mail an applet which indicates whether or not you have new mail.
You can also use it to launch your favourite mail client.

%description -l pl
ROX-Mail jest apletem sprawdzaj±cym czy masz nowe wiadomo¶ci pocztowe.
Mo¿esz tak¿e u¿ywaæ tego apletu aby uruchomiæ swojego ulubionego
klienta pocztowego.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,pixmaps}

rm -f ../install
install App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install pixmaps/*xpm $RPM_BUILD_ROOT%{_appsdir}/%{_name}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*Run
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/*.py
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/pixmaps
%dir %{_appsdir}/%{_name}
