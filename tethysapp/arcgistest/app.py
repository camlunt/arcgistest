from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgistest(TethysAppBase):
    """
    Tethys app class for ArcGIStest.
    """

    name = 'ArcGIStest'
    index = 'arcgistest:home'
    icon = 'arcgistest/images/icon.gif'
    package = 'arcgistest'
    root_url = 'arcgistest'
    color = '#53a09b'
    description = 'This is a test of ArcGIS Javascript.'
    tags = 'ArcGIS'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgistest',
                controller='arcgistest.controllers.home'
            ),
            UrlMap(
                name='bufferservice',
                url='arcgistest/bufferservice',
                controller='arcgistest.controllers.bufferservice'
            ),
            UrlMap(
                name='directions',
                url='arcgistest/directions',
                controller='arcgistest.controllers.directions'
            ),
        )

        return url_maps
