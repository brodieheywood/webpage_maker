# Brodie Heywood
# A01058795
# November 26, 2018

"""HTML5 Skeleton Generator"""


def website(user_name: str, descriptive_sentence):
    """Create a simple webpage.

    Create an HTML5 file named index.html containing a user-inputted title and description.
    PARAM: user_name, the handle of the person who created the webpage
           descriptive_sentence, a short description of what the webpage will contain
    PRECONDITION: user_name and descriptive_sentence must be strings
    POSTCONDITION: create a simple webpage framework in HTML5, outputting the content to a new index.html file
    RETURN: none
    """
    with open('index.html', 'w') as f_obj:
        f_obj.write("<!doctype html>\n"
                    "<html lang='en'>\n"
                    "<head>\n"
                    "  <meta charset='utf-8'>\n"
                    "  <title>Introduction</title>\n"
                    "  <meta name='description' content='%s’s webpage'>\n"
                    "  <meta name='author content'='%s'>\n"
                    "  <link rel='stylesheet' href='css/styles.css?v=1.0'>\n"
                    "</head>\n"
                    "<body>\n"
                    "  <center>\n"
                    "    <h1>%s</h1>\n"
                    "  </center>\n"
                    "  %s\n"
                    "</body>\n"
                    "</html>" % (user_name, user_name, user_name, descriptive_sentence))


def main():
    website('Emeril_Lagasse_Fan', 'Emeril Lagasse Fansite - BAM!')


if __name__ == '__main__':
    main()
