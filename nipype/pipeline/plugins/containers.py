import os

import networkx as nx
from nipype.pipeline.plugins.base import PluginBase
from nipype.pipeline.engine.utils import topological_sort
from nipype.interfaces.io import IOBase


class ContainerPlugin(PluginBase):

    def __init__(self,
                 plugin_args=None,
                 image=None,
                 executor=None,
                 container_args=None,
                 **kwargs):
        super(PluginBase, self).__init__(plugin_args)
        self.executor = executor
        self.image = image
        self.container_arg_key = container_arg_key


    def run(self, graph, config, image=None, updatehash=False):
        """Linearly run with container"""
        if not isinstance(graph, nx.DiGraph):
            raise ValueError('Input must be a networkx digraph object')

        old_wd = os.getcwd()
        notrun = []
        nodes, _ = topological_sort(graph)

        for node in nodes:
            try:
                if node in donotrun:
                    continue
                if self._status_callback:
                    self._status_callback(node, 'start')

                # overwrite default image
                node_img = _get_node_arg(node, 'image')
                node_exe = (self.executor if
                            not isinstance(node._interface, IOBase)
                            else None)
                node.run(updatehash=updatehash,
                         executor=node_exe,
                         image=nodeimg if node_img else self.image)

                if self._status_callback:
                    self._status_callback(node, 'end')
            except:  # broad to cover all exceptions
                os.chdir(old_wd)
                if str2bool(config['execution']['stop_on_first_crash']):
                    raise
                crashfile = report_crash(node)
                # remove dependencies from queue
                subnodes = [s for s in dfs_preorder(graph, node)]
                notrun.append(
                    dict(node=node, dependents=subnodes, crashfile=crashfile))
                donotrun.extend(subnodes)
                if self._status_callback:
                    self._status_callback(node, 'exception')
        report_nodes_not_run(notrun)


class DockerPlugin(ContainerPlugin):

    def __init__(self,
                 plugin_args=None,
                 image=None,
                 executor='docker',
                 container_arg_key='docker_args',
                 **kwargs):
        super(DockerPlugin, self).__init__(**kwargs)


    def _get_node_arg(self, node, key):
        """Parse node plugin args for docker args"""
        if (hasattr(node, "plugin_args")
                and isinstance(node.plugin_args, dict)
                and self.container_arg_key in node.plugin_args):
            dargs = dict(node.plugin_args[self.container_arg_key])
            return dargs.get(key, None)

# HELPERS

def fetch_docker_image(client, image):
    try:
        img = client.images.get(image)
    except OSError:
        print("Container %s not found on host, pulling" % image)
        img = client.images.pull(image)
    if not img:
        raise FileNotFoundError("Image %s not found" % image)
    return img
