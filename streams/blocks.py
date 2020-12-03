"""For Streamfields."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text block."""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'

# @11:20
# https://www.youtube.com/watch?v=DMP-GcElEIo&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=10&ab_channel=CodingForEverybody

class CardBlock(blocks.StructBlock):
    """Cards with image, text and buttons."""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=200)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False, help_text='If the button page above is selected, that will be used instead of the button URL.')),
            ]
        )
    )


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with Draftail features."""

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Rich Text'

class SimpleRichTextBlock(blocks.RichTextBlock):
    """Richtext with limited Draftail features."""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple Rich Text'

