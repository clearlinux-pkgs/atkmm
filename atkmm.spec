#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : atkmm
Version  : 2.24.2
Release  : 3
URL      : http://ftp.acc.umu.se/pub/GNOME/sources/atkmm/2.24/atkmm-2.24.2.tar.xz
Source0  : http://ftp.acc.umu.se/pub/GNOME/sources/atkmm/2.24/atkmm-2.24.2.tar.xz
Summary  : C++ binding for the ATK accessibility toolkit
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: atkmm-lib
Requires: atkmm-data
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(glibmm-2.4)

%description
atkmm is the C++ binding for the ATK library.
This module is part of the GNOME C++ bindings effort <http://www.gtkmm.org/>.

%package data
Summary: data components for the atkmm package.
Group: Data

%description data
data components for the atkmm package.


%package dev
Summary: dev components for the atkmm package.
Group: Development
Requires: atkmm-lib
Requires: atkmm-data
Provides: atkmm-devel

%description dev
dev components for the atkmm package.


%package lib
Summary: lib components for the atkmm package.
Group: Libraries
Requires: atkmm-data

%description lib
lib components for the atkmm package.


%prep
%setup -q -n atkmm-2.24.2

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/atkmm-1.6/proc/m4/convert.m4
/usr/lib64/atkmm-1.6/proc/m4/convert_atk.m4

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/atkmm-1.6/atkmm-1.6.devhelp2
/usr/share/doc/atkmm-1.6/reference/atkmm-1.6.tag
/usr/share/doc/atkmm-1.6/reference/html/annotated.html
/usr/share/doc/atkmm-1.6/reference/html/arrowdown.png
/usr/share/doc/atkmm-1.6/reference/html/arrowright.png
/usr/share/doc/atkmm-1.6/reference/html/bc_s.png
/usr/share/doc/atkmm-1.6/reference/html/bdwn.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Action-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Action.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Action__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Attribute-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Attribute.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Component-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Component.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Component__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Document-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Document.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Document__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1EditableText-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1EditableText.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1EditableText__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hyperlink-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hyperlink.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hyperlink__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hypertext-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hypertext.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Hypertext__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Image-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Image.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Image__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Implementor-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Implementor.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Implementor__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1NoOpObject-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1NoOpObject.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1NoOpObject__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Object-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Object.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1ObjectAccessible-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1ObjectAccessible.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1ObjectAccessible__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Object__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Range-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Range.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Relation-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Relation.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1RelationSet-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1RelationSet.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1RelationSet__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Relation__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Selection-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Selection.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Selection__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StateSet-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StateSet.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StateSet__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StreamableContent-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StreamableContent.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1StreamableContent__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Table-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Table.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Table__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Text-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Text.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1TextAttribute-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1TextAttribute.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Text__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Value-members.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Value.html
/usr/share/doc/atkmm-1.6/reference/html/classAtk_1_1Value__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classes.html
/usr/share/doc/atkmm-1.6/reference/html/classhash__load__check__resize__trigger__size__base.html
/usr/share/doc/atkmm-1.6/reference/html/classhash__load__check__resize__trigger__size__base__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/classlu__counter__policy__base.html
/usr/share/doc/atkmm-1.6/reference/html/classlu__counter__policy__base__inherit__graph.png
/usr/share/doc/atkmm-1.6/reference/html/closed.png
/usr/share/doc/atkmm-1.6/reference/html/deprecated.html
/usr/share/doc/atkmm-1.6/reference/html/dir_fb9196bee162e74bfedbd5f5874b618e.html
/usr/share/doc/atkmm-1.6/reference/html/doc.png
/usr/share/doc/atkmm-1.6/reference/html/doxygen.css
/usr/share/doc/atkmm-1.6/reference/html/doxygen.png
/usr/share/doc/atkmm-1.6/reference/html/dynsections.js
/usr/share/doc/atkmm-1.6/reference/html/folderclosed.png
/usr/share/doc/atkmm-1.6/reference/html/folderopen.png
/usr/share/doc/atkmm-1.6/reference/html/functions.html
/usr/share/doc/atkmm-1.6/reference/html/functions_c.html
/usr/share/doc/atkmm-1.6/reference/html/functions_d.html
/usr/share/doc/atkmm-1.6/reference/html/functions_e.html
/usr/share/doc/atkmm-1.6/reference/html/functions_f.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_c.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_d.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_e.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_f.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_g.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_h.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_i.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_l.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_n.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_o.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_p.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_r.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_s.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_t.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_v.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_w.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_x.html
/usr/share/doc/atkmm-1.6/reference/html/functions_func_~.html
/usr/share/doc/atkmm-1.6/reference/html/functions_g.html
/usr/share/doc/atkmm-1.6/reference/html/functions_h.html
/usr/share/doc/atkmm-1.6/reference/html/functions_i.html
/usr/share/doc/atkmm-1.6/reference/html/functions_l.html
/usr/share/doc/atkmm-1.6/reference/html/functions_n.html
/usr/share/doc/atkmm-1.6/reference/html/functions_o.html
/usr/share/doc/atkmm-1.6/reference/html/functions_p.html
/usr/share/doc/atkmm-1.6/reference/html/functions_r.html
/usr/share/doc/atkmm-1.6/reference/html/functions_s.html
/usr/share/doc/atkmm-1.6/reference/html/functions_t.html
/usr/share/doc/atkmm-1.6/reference/html/functions_type.html
/usr/share/doc/atkmm-1.6/reference/html/functions_v.html
/usr/share/doc/atkmm-1.6/reference/html/functions_vars.html
/usr/share/doc/atkmm-1.6/reference/html/functions_w.html
/usr/share/doc/atkmm-1.6/reference/html/functions_x.html
/usr/share/doc/atkmm-1.6/reference/html/functions_~.html
/usr/share/doc/atkmm-1.6/reference/html/graph_legend.html
/usr/share/doc/atkmm-1.6/reference/html/graph_legend.png
/usr/share/doc/atkmm-1.6/reference/html/group__atkmmEnums.html
/usr/share/doc/atkmm-1.6/reference/html/hierarchy.html
/usr/share/doc/atkmm-1.6/reference/html/index.html
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_0.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_1.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_2.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_3.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_4.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_5.png
/usr/share/doc/atkmm-1.6/reference/html/inherit_graph_6.png
/usr/share/doc/atkmm-1.6/reference/html/inherits.html
/usr/share/doc/atkmm-1.6/reference/html/jquery.js
/usr/share/doc/atkmm-1.6/reference/html/modules.html
/usr/share/doc/atkmm-1.6/reference/html/namespaceAtk.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_b.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_c.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_enum.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_eval.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_eval_r.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_eval_s.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_eval_t.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_eval_x.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_func.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_i.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_l.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_r.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_s.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_t.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_type.html
/usr/share/doc/atkmm-1.6/reference/html/namespacemembers_x.html
/usr/share/doc/atkmm-1.6/reference/html/namespaces.html
/usr/share/doc/atkmm-1.6/reference/html/nav_f.png
/usr/share/doc/atkmm-1.6/reference/html/nav_g.png
/usr/share/doc/atkmm-1.6/reference/html/nav_h.png
/usr/share/doc/atkmm-1.6/reference/html/open.png
/usr/share/doc/atkmm-1.6/reference/html/pages.html
/usr/share/doc/atkmm-1.6/reference/html/since_1_12.html
/usr/share/doc/atkmm-1.6/reference/html/since_1_3.html
/usr/share/doc/atkmm-1.6/reference/html/since_1_9.html
/usr/share/doc/atkmm-1.6/reference/html/since_2_10.html
/usr/share/doc/atkmm-1.6/reference/html/since_2_12.html
/usr/share/doc/atkmm-1.6/reference/html/since_2_24.html
/usr/share/doc/atkmm-1.6/reference/html/splitbar.png
/usr/share/doc/atkmm-1.6/reference/html/structAtk_1_1AttributeTraits-members.html
/usr/share/doc/atkmm-1.6/reference/html/structAtk_1_1AttributeTraits.html
/usr/share/doc/atkmm-1.6/reference/html/sync_off.png
/usr/share/doc/atkmm-1.6/reference/html/sync_on.png
/usr/share/doc/atkmm-1.6/reference/html/tab_a.png
/usr/share/doc/atkmm-1.6/reference/html/tab_b.png
/usr/share/doc/atkmm-1.6/reference/html/tab_h.png
/usr/share/doc/atkmm-1.6/reference/html/tab_s.png
/usr/share/doc/atkmm-1.6/reference/html/tabs.css

%files dev
%defattr(-,root,root,-)
/usr/include/atkmm-1.6/atkmm.h
/usr/include/atkmm-1.6/atkmm/action.h
/usr/include/atkmm-1.6/atkmm/component.h
/usr/include/atkmm-1.6/atkmm/document.h
/usr/include/atkmm-1.6/atkmm/editabletext.h
/usr/include/atkmm-1.6/atkmm/hyperlink.h
/usr/include/atkmm-1.6/atkmm/hypertext.h
/usr/include/atkmm-1.6/atkmm/image.h
/usr/include/atkmm-1.6/atkmm/implementor.h
/usr/include/atkmm-1.6/atkmm/init.h
/usr/include/atkmm-1.6/atkmm/noopobject.h
/usr/include/atkmm-1.6/atkmm/object.h
/usr/include/atkmm-1.6/atkmm/objectaccessible.h
/usr/include/atkmm-1.6/atkmm/private/action_p.h
/usr/include/atkmm-1.6/atkmm/private/component_p.h
/usr/include/atkmm-1.6/atkmm/private/document_p.h
/usr/include/atkmm-1.6/atkmm/private/editabletext_p.h
/usr/include/atkmm-1.6/atkmm/private/hyperlink_p.h
/usr/include/atkmm-1.6/atkmm/private/hypertext_p.h
/usr/include/atkmm-1.6/atkmm/private/image_p.h
/usr/include/atkmm-1.6/atkmm/private/implementor_p.h
/usr/include/atkmm-1.6/atkmm/private/noopobject_p.h
/usr/include/atkmm-1.6/atkmm/private/object_p.h
/usr/include/atkmm-1.6/atkmm/private/objectaccessible_p.h
/usr/include/atkmm-1.6/atkmm/private/range_p.h
/usr/include/atkmm-1.6/atkmm/private/relation_p.h
/usr/include/atkmm-1.6/atkmm/private/relationset_p.h
/usr/include/atkmm-1.6/atkmm/private/selection_p.h
/usr/include/atkmm-1.6/atkmm/private/stateset_p.h
/usr/include/atkmm-1.6/atkmm/private/streamablecontent_p.h
/usr/include/atkmm-1.6/atkmm/private/table_p.h
/usr/include/atkmm-1.6/atkmm/private/text_p.h
/usr/include/atkmm-1.6/atkmm/private/value_p.h
/usr/include/atkmm-1.6/atkmm/range.h
/usr/include/atkmm-1.6/atkmm/relation.h
/usr/include/atkmm-1.6/atkmm/relationset.h
/usr/include/atkmm-1.6/atkmm/selection.h
/usr/include/atkmm-1.6/atkmm/stateset.h
/usr/include/atkmm-1.6/atkmm/streamablecontent.h
/usr/include/atkmm-1.6/atkmm/table.h
/usr/include/atkmm-1.6/atkmm/text.h
/usr/include/atkmm-1.6/atkmm/value.h
/usr/include/atkmm-1.6/atkmm/wrap_init.h
/usr/lib64/*.so
/usr/lib64/atkmm-1.6/include/atkmmconfig.h
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
