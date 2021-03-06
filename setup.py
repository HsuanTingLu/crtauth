# Copyright (c) 2011-2017 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.core import setup

setup(
    name='crtauth',
    version='0.99.4',
    description="A public key backed client/server authentication system",
    author='Noa Resare',
    author_email='noa@spotify.com',
    license='Apache-2.0',
    packages=['crtauth'],
    install_requires=['msgpack-python>=0.4.0']
)
