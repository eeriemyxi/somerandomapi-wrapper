"""
**[UNFINISHED]** An API wrapper for some-random-api.ml

License
-------
MIT License

Copyright (c) 2021 Myxi | some-random-api.ml API Wrapper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from . import http
from .structures.animal import Animal, AnimalResponse
from .structures.anime import Anime
from .structures.fact import Fact
from .structures.filters import Filter
from .structures.image import Image
from .structures.others import MC, Lyrics, MCNameHistory, Meme, Other
from .structures.welcome import welcome as Welcome

__all__ = [
    "Animal",
    "AnimalResponse",
    "Anime",
    "Filter",
    "Other",
    "Fact",
    "Image",
    "Welcome",
    "MC",
    "Lyrics",
    "Meme",
    "MCNameHistory",
]

