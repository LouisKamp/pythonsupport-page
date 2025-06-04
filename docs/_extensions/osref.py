from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx import addnodes

# Use: :osref:`label <fallback|win|mac|linux>`
def osref_role(name, rawtext, link_text, lineno, inliner, options={}, content=[]):
    
    env = inliner.document.settings.env

    try:
        link_text, targets = link_text.split('<', 1)
        link_text = link_text.strip()
        targets = targets.rstrip('>').strip()
        parts = targets.split('|')
    except ValueError:
        msg = inliner.reporter.error(
            f"Invalid osref format. Use: `label <fallback|win|mac|linux>`",
            line=lineno)
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    
    fallback_label  = parts[0] if len(parts) > 0 else '#'
    windows_label   = parts[1] if len(parts) > 1 else fallback_label
    macos_label     = parts[2] if len(parts) > 2 else fallback_label
    linux_label     = parts[3] if len(parts) > 3 else fallback_label

    def create_link(label, os=None, hide=True):
        pnode = addnodes.pending_xref()
        pnode['refdoc'] = env.docname
        pnode['reftype'] = 'ref'       # Standard ref type
        pnode['reftarget'] = label
        pnode['refdomain'] = 'std'     # Standard domain for :ref:
        pnode['refexplicit'] = True
        pnode['ids'].append(f"osref-{env.new_serialno('osref')}")
        if os:
            pnode['classes'].append(f'os-{os}')
        if hide:
            pnode['classes'].append('osref-hide')
        else:
            pnode['classes'].append('osref-show')
        
        pnode += nodes.inline(link_text, link_text)

        return pnode


    return [create_link(windows_label, "windows"), create_link(macos_label, "macos"), create_link(linux_label, "linux"), create_link(fallback_label, hide=False)], []


def setup(app):
    app.add_role("osref", osref_role)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }