# -*- coding: utf-8 -*-

def print_MP4_atoms(fname):
    # NOTE: The following websites have some very useful information on how to
    #       parse MP4 files - the first just forgot to say that integers are
    #       big-endian.
    #         * http://atomicparsley.sourceforge.net/mpeg-4files.html
    #         * https://wiki.multimedia.cx/index.php/QuickTime_container

    # Import modules ...
    import numpy
    import os
    import re

    # Load sub-functions ...
    from .convert_bytes_to_pretty_bytes import convert_bytes_to_pretty_bytes

    # Open MP4 read-only ...
    with open(fname, "rb") as fobj:
        # Set trigger ...
        found = False

        # Loop over entire contents of MP4 ...
        while True:
            # Attempt to read 4 bytes as a big-endian un-signed 32 bit integer and stop looping if it failed ...
            arr = numpy.fromstring(fobj.read(4), dtype = numpy.uint32).byteswap()
            off = 4
            if arr.size != 1:
                break

            # Extract atom name ...
            name = fobj.read(4)
            off += 4

            # Check that it matches the pattern ...
            if re.match(r"[a-z][a-z][a-z][a-z]", name) is None:
                print u"ERROR: \"{0:s}\" is not an atom name in \"{1:s}\"".format(name, fname)
                return

            # Check that it is a MP4 file ...
            if found == False and name != "ftyp":
                print u"ERROR: \"{0:s}\" is not a MP4".format(fname)
                return
            else:
                found = True

            # Check the length ...
            if arr[0] == 0:
                # NOTE: This atom runs until EOF.

                # Print summary ...
                print u"{0:s} is the remainder of the file".format(name)

                # Stop looping ...
                break
            elif arr[0] == 1:
                # NOTE: This atom has 64-bit sizes.

                # Attempt to read 8 bytes as a big-endian un-signed 64 bit integer ...
                arr = numpy.fromstring(fobj.read(8), dtype = numpy.uint64).byteswap()
                off += 8
                if arr.size != 1:
                    print u"ERROR: failed to read 64-bit size in \"{0:s}\"".format(fname)
                    return

            # Print summary ...
            size, units = convert_bytes_to_pretty_bytes(arr[0])
            print u"{0:s} is {1:6.1f} {2:3s} long (as an {3:s} atom)".format(name, size, units, arr.dtype)

            # Skip to the end of the atom ...
            fobj.seek(arr[0] - off, os.SEEK_CUR)
