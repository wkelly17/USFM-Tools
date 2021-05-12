class Error(Exception):
    """Base class for other exceptions."""

    pass


class MalformedUsfmError(Error):
    """Raised when a USFM file does not include an 'id' element or the
    book code, e.g., 'gal', is not valid, id value is not defined in
    silNames in books.py."""

    pass
