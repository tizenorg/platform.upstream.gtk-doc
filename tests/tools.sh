#!/bin/sh

suite="tools"

failed=0
tested=0

echo "Running suite(s): gtk-doc-$suite";

# we can use which here as we override the path in TEST_ENVIRONMENT

# test perl scripts
for file in gtkdoc-check gtkdoc-fixxref gtkdoc-mkdb gtkdoc-mktmpl gtkdoc-rebase gtkdoc-scan gtkdoc-scangobj gtkdoc-scanobj ; do
  /usr/bin/perl -cwT `which $file`
  if test $? = 1 ; then failed=$(($failed + 1)); fi
  tested=$(($tested + 1))
done


# test shell scripts
for file in gtkdoc-mkhtml gtkdoc-mkman gtkdoc-mkpdf gtkdocize; do
  sh -n `which $file`
  if test $? != 0 ; then failed=$(($failed + 1)); fi
  tested=$(($tested + 1))
done


# test xsl files
for file in $ABS_TOP_SRCDIR/*.xsl; do
  xmllint --noout --noent $file
  if test $? != 0 ; then failed=$(($failed + 1)); fi
  tested=$(($tested + 1))
done

# summary

rate=$((100*($tested - $failed)/$tested));
echo "$rate %: Checks $tested, Failures: $failed"

test $failed = 0
exit $?
