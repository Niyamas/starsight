"""For Streamfields."""

from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text block."""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'

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