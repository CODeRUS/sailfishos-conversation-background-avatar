# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-conversation-background-avatar

# >> macros
BuildArch: noarch
# << macros

Summary:    Conversation background avatar
Version:    0.0.2
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   jolla-messages >= 0.4.31.3

%description
Patch for showing contact avatar in conversation background


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-conversation-background-avatar
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-conversation-background-avatar
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-conversation-background-avatar || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-conversation-background-avatar || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-conversation-background-avatar
# >> files
# << files
