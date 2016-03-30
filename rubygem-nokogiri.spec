#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-nokogiri
Version  : 1.6.6.2
Release  : 7
URL      : https://rubygems.org/downloads/nokogiri-1.6.6.2.gem
Source0  : https://rubygems.org/downloads/nokogiri-1.6.6.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-nokogiri-bin
Requires: rubygem-nokogiri-lib
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-hoe-debugging
BuildRequires : rubygem-hoe-git
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rexical
BuildRequires : zlib-dev

%description
= Nokogiri {<img src="https://secure.travis-ci.org/sparklemotion/nokogiri.png?rvm=1.9.3" />}[http://travis-ci.org/sparklemotion/nokogiri] {<img src="https://codeclimate.com/github/sparklemotion/nokogiri.png" />}[https://codeclimate.com/github/sparklemotion/nokogiri] {<img src="https://www.versioneye.com/ruby/nokogiri/badge.png" alt="Dependency Status" />}[https://www.versioneye.com/ruby/nokogiri]

%package bin
Summary: bin components for the rubygem-nokogiri package.
Group: Binaries

%description bin
bin components for the rubygem-nokogiri package.


%package lib
Summary: lib components for the rubygem-nokogiri package.
Group: Libraries

%description lib
lib components for the rubygem-nokogiri package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n nokogiri-1.6.6.2
gem spec %{SOURCE0} -l --ruby > rubygem-nokogiri.gemspec

%build
gem build rubygem-nokogiri.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
nokogiri-1.6.6.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/nokogiri-1.6.6.2
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/nokogiri-1.6.6.2.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/nokogiri-1.6.6.2/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/nokogiri-1.6.6.2/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/nokogiri-1.6.6.2/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/.cross_rubies
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/.editorconfig
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/CHANGELOG.ja.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/C_CODING_STYLE.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/README.ja.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ROADMAP.md
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/STANDARD_RESPONSES.md
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/Y_U_NO_GEMSPEC.md
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/bin/nokogiri
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/build_all
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/dependencies.yml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/.RUBYARCHDIR.-.nokogiri.time
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/depend
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_document.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_document.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_document.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_element_description.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_element_description.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_element_description.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_entity_lookup.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_entity_lookup.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_entity_lookup.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_parser_context.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_parser_context.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_parser_context.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_push_parser.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_push_parser.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/html_sax_push_parser.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/nokogiri.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/nokogiri.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/nokogiri.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attr.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attr.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attr.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attribute_decl.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attribute_decl.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_attribute_decl.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_cdata.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_cdata.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_cdata.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_comment.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_comment.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_comment.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document_fragment.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document_fragment.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_document_fragment.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_dtd.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_dtd.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_dtd.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_content.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_content.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_content.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_decl.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_decl.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_element_decl.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_encoding_handler.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_encoding_handler.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_encoding_handler.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_decl.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_decl.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_decl.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_reference.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_reference.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_entity_reference.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_io.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_io.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_io.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_libxml2_hacks.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_libxml2_hacks.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_libxml2_hacks.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_namespace.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_namespace.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_namespace.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node_set.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node_set.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_node_set.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_processing_instruction.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_processing_instruction.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_processing_instruction.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_reader.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_reader.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_reader.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_relax_ng.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_relax_ng.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_relax_ng.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser_context.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser_context.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_parser_context.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_push_parser.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_push_parser.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_sax_push_parser.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_schema.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_schema.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_schema.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_syntax_error.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_syntax_error.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_syntax_error.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_text.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_text.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_text.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_xpath_context.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_xpath_context.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xml_xpath_context.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xslt_stylesheet.c
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xslt_stylesheet.h
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/xslt_stylesheet.o
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/parser.y
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/parser_extras.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/tokenizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/tokenizer.rex
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/css/xpath_visitor.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/decorators/slop.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/element_description.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/element_description_defaults.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/entity_lookup.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/sax/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/sax/parser_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/html/sax/push_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/attr.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/attribute_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/cdata.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/character_data.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/dtd.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/element_content.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/element_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/entity_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/namespace.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/node/save_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/node_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/notation.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/parse_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/pp.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/pp/character_data.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/pp/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/processing_instruction.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/reader.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/relax_ng.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/sax.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/sax/document.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/sax/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/sax/parser_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/sax/push_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/schema.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/searchable.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/text.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/xpath.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/xpath/syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xml/xpath_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xslt.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/xslt/stylesheet.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/xsd/xmlparser/nokogiri.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/suppressions/README.txt
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/suppressions/nokogiri_ree-1.8.7.358.supp
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/suppressions/nokogiri_ruby-1.8.7.370.supp
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/suppressions/nokogiri_ruby-1.9.2.320.supp
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/suppressions/nokogiri_ruby-1.9.3.327.supp
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/tasks/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/css/test_nthiness.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/css/test_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/css/test_tokenizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/css/test_xpath_visitor.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/decorators/test_slop.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/2ch.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/address_book.rlx
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/address_book.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/atom.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/bar/bar.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/bogus.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/dont_hurt_em_why.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/encoding.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/encoding.xhtml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/exslt.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/exslt.xslt
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/foo/foo.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/metacharset.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/noencoding.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/po.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/po.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/saml/saml20assertion_schema.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/saml/saml20protocol_schema.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/saml/xenc_schema.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/saml/xmldsig_schema.xsd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/shift_jis.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/shift_jis.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/shift_jis_no_charset.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/slow-xpath.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/snuggles.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/staff.dtd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/staff.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/staff.xslt
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/test_document_url/bar.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/test_document_url/document.dtd
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/test_document_url/document.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/tlm.html
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/to_be_xincluded.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/valid_bar.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/files/xinclude.xml
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/sax/test_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/sax/test_parser_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/sax/test_push_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_document.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_document_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_element_description.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_named_characters.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/html/test_node_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_additional_namespaces_in_builder_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_aliased_default.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_in_builder_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_in_cloned_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_in_created_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_in_parsed_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/namespaces/test_namespaces_preservation.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_convert_xpath.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_css_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_encoding_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_memory_leak.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_nokogiri.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_reader.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_soap4r_sax.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/test_xslt_transforms.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/node/test_save_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/node/test_subclass.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/sax/test_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/sax/test_parser_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/sax/test_push_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_attr.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_attribute_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_c14n.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_cdata.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_comment.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_document.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_document_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_document_fragment.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_dtd.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_dtd_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_element_content.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_element_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_entity_decl.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_entity_reference.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_namespace.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node_attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node_inheritance.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node_reparenting.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_node_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_parse_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_processing_instruction.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_reader_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_relax_ng.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_schema.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_syntax_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_text.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_unparented_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_xinclude.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xml/test_xpath.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xslt/test_custom_functions.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test/xslt/test_exception_handling.rb
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/test_all
/usr/lib64/ruby/gems/2.3.0/specifications/nokogiri-1.6.6.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/nokogiri

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/nokogiri-1.6.6.2/nokogiri/nokogiri.so
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/ext/nokogiri/nokogiri.so
/usr/lib64/ruby/gems/2.3.0/gems/nokogiri-1.6.6.2/lib/nokogiri/nokogiri.so
