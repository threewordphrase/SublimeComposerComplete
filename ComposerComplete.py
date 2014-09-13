import sublime, sublime_plugin
import os

class ComposerComplete(sublime_plugin.EventListener):

	def on_query_completions(self, view, prefix, locations):
		results = []
		classmap_path = view.window().folders()[0]+"/vendor/composer/autoload_classmap.php"
		f=os.popen("grep -i '"+prefix+"' '"+classmap_path+"' | awk '{ print $1 }'")
		for i in f.readlines():
			string = i.strip().replace('\\\\', '\\')
			string = string.replace("'", '')
			results.append((string, string,))
		return results
