**mdi-svg-as-json** Downloads and saves a json file containing all currently supported *Material Design Icons* and their SVG path from https://pictogrammers.com/library/mdi.

Current MDI version in this dump: **7.4.47**

## Usage

* The list of all icons with their SVG paths is delivered from the pictogrammers server in a JSON file. The URL of the file is hard-coded in this script. As long as this URL does not change on the server, you only need to run the script to get all current icons.
* If the URL changes - which seems likely - it is easy enough to get the new URL: it is (at least for now) the largest file being loaded when visiting the Pictogrammers page.
![Streamdeck UI Usage Example](image/network-monitor.png)
* If you want to create a valid SVG structure from a path you need to put it in an XML structure like  
`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>{title}</title><path d="{path}" /></svg>`  
e. g. for "lightbulb" it would look like  
`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>lightbulb</title><path d="M12,2A7,7 0 0,0 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H15A1,1 0 0,0 16,17V14.74C17.81,13.47 19,11.38 19,9A7,7 0 0,0 12,2M9,21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9V21Z" /></svg>`