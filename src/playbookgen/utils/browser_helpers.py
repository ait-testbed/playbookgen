from playwright.sync_api import ElementHandle


def build_naive_css_selector(element: ElementHandle) -> str:
    """
    naive CSS selector builder by climbing up DOM parents
    """
    return element.evaluate(
        """
        (el) => {
            function getSelector(node) {
                // If the node is the document or the HTML element, stop.
                if (!node || node.nodeType !== Node.ELEMENT_NODE) return '';
                let selector = node.tagName.toLowerCase();

                // If it has an ID, use that and stop climbing.
                if (node.id) {
                    selector += '#' + node.id;
                    return selector;
                }

                // Otherwise, if it has a class, include the first class as a partial reference.
                if (node.className) {
                    const className = node.className.trim().split(' ')[0];
                    if (className) {
                        selector += '.' + className;
                    }
                }

                const parent = node.parentElement;
                if (!parent) {
                    return selector;
                }

                // Count how many siblings of the same type precede the node.
                let index = 1;
                let sibling = node.previousElementSibling;
                while (sibling) {
                    if (sibling.tagName === node.tagName) {
                        index += 1;
                    }
                    sibling = sibling.previousElementSibling;
                }

                // Append :nth-of-type if needed.
                selector += ':nth-of-type(' + index + ')';

                // Recursively go up the tree.
                return getSelector(parent) + ' > ' + selector;
            }

            return getSelector(el);
        }
        """
    )
