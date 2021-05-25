"""
Display stream
==============
Defining methods to format data that will appear in the terminal. 
"""


from colorama import (
    Fore,
    Style
)
from prettytable import PrettyTable

class DisplayStream():
    """
    Methods to format and display Reddit stream objects.
    """

    @staticmethod
    def _populate_table(include_fields, obj, prefix, pretty_stream):
        """
        Populate the PrettyTable rows with Reddit object metadata.

        Parameters
        ----------
        include_fields: list
            List containing dictionary keys that will be added to the PrettyTable
            row
        obj: dict
            Dictionary containing Reddit comment or submission data
        prefix: str
            String denoting a prefix to prepend to an attribute
        pretty_stream: PrettyTable instance

        Returns
        -------
        None
        """

        for attribute, data in obj.items():
            if attribute in include_fields:
                pretty_stream.add_row([
                    prefix + attribute,
                    data
                ])

    @staticmethod
    def display(obj):
        """
        Format and print string containing stream information.

        Parameters
        ----------
        obj: dict
            Dictionary containing Reddit comment or submission data

        Returns
        -------
        None
        """

        pretty_stream = PrettyTable()
        pretty_stream.field_names = [
            "%s Attribute" % obj["type"].capitalize(),
            "Data"
        ]

        if obj["type"] == "submission":
            include_fields = [
                "author",
                "created_utc",
                "distinguished",
                "edited",
                "id",
                "is_original_content",
                "is_self",
                "link_flair_text",
                "nsfw",
                "score",
                "selftext",
                "spoiler",
                "stickied",
                "title",
                "url"
            ]
        elif obj["type"] == "comment":
            include_fields = [
                "author",
                "body",
                "created_utc",
                "distinguished",
                "edited",
                "id",
                "is_submitter",
                "link_id",
                "parent_id",
                "score",
                "stickied"
            ]
            
            submission_fields = [
                "created_utc",
                "nsfw",
                "num_comments",
                "score",
                "title",
                "upvote_ratio",
                "url",
            ]

            DisplayStream._populate_table(submission_fields, obj["submission"], "submission_", pretty_stream)

        DisplayStream._populate_table(include_fields, obj, "", pretty_stream)

        pretty_stream.sortby = "%s Attribute" % obj["type"].capitalize()
        pretty_stream.align = "l"
        pretty_stream.max_width = 120

        print(pretty_stream)
