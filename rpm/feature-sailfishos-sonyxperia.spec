# Feature Organisation
# Right now the feauture package is build under the sony kumano Organisation.
# In case the layout differs `sailfishosorg_adaptationOrg` can be set to any organisation.
# For example project foobar with subproject bar this would be 'foobar:/bar'.

%if 0%{!?featureOrg:1}
%global featureOrg sony:/kumano:/customers:/sailfishos-sonyxperia
%endif

Name: feature-sailfishos-sonyxperia
Version: 0
Release: 1
Summary: Feature package for packages build on for SailfishOS Sony-Xperia community ports
URL: https://github.com/SailfishOS-SonyXperia
License: GPLv2
Source0: %{name}-%{version}.tar.gz
Requires(post): coreutils
BuildArch: noarch

# Content for this customer pattern
# NOTE: Remember to add also BuildRequires
Requires: jolla-settings-accounts-extensions-3rd-party-all
Requires: patterns-sailfish-consumer-generic
Requires: ssu-vendor-data-sailfishosorg

# Add requires here as well to make sure version is built last in feature repo
BuildRequires: jolla-settings-accounts-extensions-3rd-party-all
BuildRequires: patterns-sailfish-consumer-generic
BuildRequires: ssu-vendor-data-sailfishosorg

%description
%{summary}.


%prep
%setup -q

%build

%install
# Put the version to the feature ini file.
mkdir -p %{buildroot}%{_datadir}/ssu/features.d/
sed \
    -e s/@VERSION@/%{version}-%{release}/g \
    -e "s|@featureOrg@|%{featureOrg}|g" \
    -e "s/@DESCRIPTION@/%{summary}/g" \
    features/customer-sailfishos-sonyxperia.ini > %{buildroot}%{_datadir}/ssu/features.d/customer-sailfishos-sonyxperia.ini


install -Dm644 zypp/%{name}.check %{buildroot}%{_sysconfdir}/zypp/systemCheck.d/%{name}.check

%post
touch %{_datadir}/ssu/features.d/*.ini


%files
%defattr(-,root,root,-)
# Do not verify the time as we are touching the file on post
%verify (not mtime) %{_datadir}/ssu/features.d/*.ini
%{_sysconfdir}/zypp/systemCheck.d/%{name}.check
