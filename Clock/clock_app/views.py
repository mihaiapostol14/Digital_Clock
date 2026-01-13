from django.views.generic import TemplateView

from .utils import ClockMixin


class ClockView(ClockMixin, TemplateView):
    template_name = 'clock_app/clock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context, title='Digital Clock')