from django.contrib.contenttypes.models import ContentType

from .models import MenuItem


def get_navigation_node_for_content_object(menu_content, content_object, node_model=MenuItem):
    """
    Find a navigation node that contains a content_object in a Navigation menu

    :param menu_content: A MenuContent instance
    :param content_object: A content object registered in the cms_config
    :param node_model: A model used for a navigation item
    :return: A navigation node or False
    """

    root = node_model.get_root_nodes().filter(menucontent=menu_content).first()
    if root:
        content_object_content_type = ContentType.objects.get_for_model(content_object)
        child_nodes = root.get_descendants()
        search_node = child_nodes.filter(content_type=content_object_content_type, object_id=content_object.pk).first()
        if search_node:
            return search_node

    return False
