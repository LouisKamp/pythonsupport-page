from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx import addnodes

# Define a custom node
class OSLinkNode(nodes.General, nodes.Element):
    pass

# Define a directive that adds the custom node
class OSLinkDirective(SphinxDirective):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'windows': str,
        'linux': str,
        'macos': str,
        'fallback': str
    }

    def run(self):
        node = OSLinkNode()
        node['link_text'] = self.arguments[0]
        node['win_url'] = self.options.get('windows', '#')
        node['linux_url'] = self.options.get('linux', '#')
        node['macos_url'] = self.options.get('macos', '#')
        node['fallback_url'] = self.options.get('fallback', '#')

        node['id'] = f"oslink-{self.env.new_serialno('oslink')}"
        return [node]

# 3. HTML translator function
def html_visit_oslink_node(self, node):
    link_text = node['link_text']
    node_id = node['id']
    mac_url = node.get('macos_url', '#')
    linux_url = node.get('linux_url', '#')
    win_url = node.get('win_url', '#')
    fallback_url = node.get('fallback_url', '#')
    self.body.append(f'''
        <a id="{node_id}" class="reference internal" href="{fallback_url}"><span class="std std-ref">{link_text}</span></a>
        <script>
        (function() {{
            var el = document.getElementById("{node_id}");
            var platform = navigator.platform.toLowerCase();
            var href = "{fallback_url}";

            if (platform.includes("win")) {{
                href = "{win_url}";
            }} else if (platform.includes("mac")) {{
                href = "{mac_url}";
            }} else {{
                href = "{linux_url}";
            }}

            el.href = href;
        }})();
        </script>
    ''')

def html_depart_oslink_node(self, node):
    pass  # no closing needed


def oslink_role(name, rawtext, link_text, lineno, inliner, options={}, content=[]):
    env = inliner.document.settings.env
    app = env.app
    serial = env.new_serialno('oslink')
    try:
        link_text, targets = link_text.split('<', 1)
        link_text = link_text.strip()
        targets = targets.rstrip('>').strip()
        parts = targets.split('|')
    except ValueError:
        msg = inliner.reporter.error(
            f"Invalid oslink format. Use: `label <win|mac|linux|fallback>`",
            line=lineno)
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    
    windows_label   = parts[0] if len(parts) > 0 else None
    macos_label     = parts[1] if len(parts) > 1 else None
    linux_label     = parts[2] if len(parts) > 2 else None
    fallback_label  = parts[3] if len(parts) > 3 else '#'

    def create_link(label, os=None, hide=True):
        pnode = addnodes.pending_xref()
        pnode['refdoc'] = env.docname
        pnode['reftype'] = 'ref'       # Standard ref type
        pnode['reftarget'] = label
        pnode['refdomain'] = 'std'     # Standard domain for :ref:
        pnode['refexplicit'] = True
        pnode['ids'].append(f"oslink-{env.new_serialno('oslink')}")
        if os:
            pnode['classes'].append(f'os-{os}')
        if hide:
            pnode['classes'].append('oslink-hide')
        else:
            pnode['classes'].append('oslink-show')
        
        pnode += nodes.inline(link_text, link_text)

        return pnode


    return [create_link(windows_label, "windows"), create_link(macos_label, "macos"), create_link(linux_label, "linux"), create_link(fallback_label, hide=False)], []


def setup(app):
    app.add_node(OSLinkNode, html=(html_visit_oslink_node, html_depart_oslink_node))
    app.add_directive("oslink", OSLinkDirective)
    app.add_role("oslink", oslink_role)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }