import unittest
from gradescope_utils.autograder_utils.decorators import number, weight
from gradescope_utils.autograder_utils.files import check_submitted_files


class TestFiles(unittest.TestCase):
    """Entry point for the autograder. Worth 10 points in Gradescope."""

    @number("1.1")
    @weight(10.0)
    def test_submitted_files(self):
        """Test for required files and folders."""

        required_files = check_submitted_files([
            'data/sample.txt',
            'app.py',
            'dictogram.py',
            'hashtable.py',
            'linkedlist.py',
            'listogram.py',
            'requirements.txt',
            'runtime.txt',
            'Procfile'
        ])

        output = """\n\n
⚠️ NOTE: Your solution must contain the following files.
         Here's an example of the repository structure we set up in class.

📂 ACS-1120-Intro-Data-Structures   <- SUBMIT THIS FOLDER!
    ├── 📂 Code                     <- DO NOT SUBMIT!
        ├── 📂 data
            └── sample.txt          <- A few paragraphs of your corpus.
        ├── app.py
        ├── dictogram.py
        ├── hashtable.py
        ├── linkedlist.py
        ├── listogram.py
        ├── requirements.txt
        ├── runtime.txt
        └── Procfile"""

        self.assertEqual(len(required_files), 9,
                         'MISSING REQUIRED FILES\n\n' +
                         ',\n'.join(required_files)
                         + output)
