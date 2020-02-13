"""
awslimitchecker/tests/alerts/test_dummy.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

################################################################################
Copyright 2015-2019 Jason Antman <jason@jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/awslimitchecker> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""

from awslimitchecker.alerts.dummy import Dummy


class TestDummy(object):

    def test_init(self):
        cls = Dummy('foo')
        assert cls._region_name == 'foo'

    def test_on_success(self, capsys):
        Dummy('foo').on_success(duration=1.2)
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found no problems\n' \
                      'awslimitchecker run duration: 1.2\n'

    def test_on_success_no_duration(self, capsys):
        Dummy('foo').on_success()
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found no problems\n'

    def test_on_critical(self, capsys):
        Dummy('foo').on_critical(None, 'probstr', duration=1.2)
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found CRITICALS:\n' \
                      'probstr\n' \
                      'awslimitchecker run duration: 1.2\n'

    def test_on_critical_no_duration(self, capsys):
        Dummy('foo').on_critical(None, 'probstr')
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found CRITICALS:\n' \
                      'probstr\n'

    def test_on_critical_exception(self, capsys):
        exc = RuntimeError('bar')
        Dummy('foo').on_critical(None, None, exc=exc)
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo failed with exception: ' \
                      '%s\n' % exc.__repr__()

    def test_on_warning(self, capsys):
        Dummy('foo').on_warning(None, 'probstr', duration=1.2)
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found WARNINGS:\n' \
                      'probstr\n' \
                      'awslimitchecker run duration: 1.2\n'

    def test_on_warning_no_duration(self, capsys):
        Dummy('foo').on_warning(None, 'probstr')
        out, _ = capsys.readouterr()
        assert out == 'awslimitchecker in foo found WARNINGS:\n' \
                      'probstr\n'