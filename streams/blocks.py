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

    class Meta:
        template = 'streams/card_block.html'
        icon = 'placeholder'
        label = 'Staff Cards'


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with Draftail features."""

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Rich Text'

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'h2',
            'h3',
            'h4',
            'superscript',
            'subscript',
            #'center',
            'ol',
            'ul',
            'hr',
            'link',
            'document-link',
            'image',
            'embed',
            'code',
            'redo',
            'undo',
        ]

class SimpleRichTextBlock(blocks.RichTextBlock):
    """Richtext with limited Draftail features."""

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Simple Rich Text'

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            'bold',
            'italic',
            'link',
        ]


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=False, max_length=60)
    text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
        template = 'streams/cta_block.html'
        icon = 'placeholder'
        label = 'Call to Action'


class LinkStructValue(blocks.StructValue):
    """
    Additional logic for the ButtonBlock() urls. Adds a method
    that returns a button link to a page or a URL. Prioritizes
    the button page. In the template, reference the method with:
    {{ self.url }}
    """

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')

        """ if button_page and not button_url:
            return button_page.url

        elif button_url and not button_page:
            return button_url

        elif button_page and button_url:
            return button_page.url """

        # better than above, incorporates priority for button_page too
        if button_page:
            return button_page.url

        elif button_url:
            return button_url

        return None

class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""

    button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this URL will be used first.')
    button_url = blocks.URLBlock(required=False, help_text='If added, this URL will be used second.')

    class Meta:
        template = 'streams/button_block.html'
        icon = 'placeholder'
        label = 'Single Button'
        value_class = LinkStructValue

    """ def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['newest_posts'] = ArticleDetailPage.objects.live().public()[:3]
        return context """