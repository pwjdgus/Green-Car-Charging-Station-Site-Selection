import folium
import pandas as pd

# my_pos = [35.1154117, 128.9675937]
# ## open street map
# map_osm = folium.Map(
#     location= my_pos,
#     zoom_start=17
# )
#
# html = '''<body style="background-color:#A0B3C4;">
#         <iframe src="final_fig.html" style="background-color: #E9EEF6 "font-family:'NanumSquare'; " width="250" height="250"  frameborder="0" >
#         </body>
#         '''
# #
# iframe = folium.IFrame(html,
#                        width=100,
#                        height=100)
# popup = folium.Popup(folium.Html(html, script=True, width=250, height=250))
# folium.Marker(my_pos, popup=popup).add_to(map_osm)
# map_osm.save('map_final.html')
