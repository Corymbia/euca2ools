# Copyright (c) 2009-2016 Hewlett Packard Enterprise Development LP
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from requestbuilder import Arg
from requestbuilder.response import PaginatedResponse

from euca2ools.commands.iam import IAMRequest, AS_ACCOUNT


class ListUsers(IAMRequest):
    DESCRIPTION = "List your account's users"
    ARGS = [Arg('-p', '--path-prefix', dest='PathPrefix', metavar='PREFIX',
                help='limit results to users who begin with a given path'),
            AS_ACCOUNT]
    LIST_TAGS = ['Users']

    def main(self):
        return PaginatedResponse(self, (None,), ('Users',))

    def prepare_for_page(self, page):
        # Pages are defined by markers
        self.params['Marker'] = page

    # pylint: disable=no-self-use
    def get_next_page(self, response):
        if response.get('IsTruncated') == 'true':
            return response['Marker']
    # pylint: enable=no-self-use

    # pylint: disable=no-self-use
    def print_result(self, result):
        for user in result.get('Users', []):
            print user['Arn']
    # pylint: enable=no-self-use
