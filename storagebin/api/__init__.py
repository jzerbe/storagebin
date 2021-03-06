from storagebin.internal import DELETE as int_DELETE
from storagebin.internal import GET as int_GET
from storagebin.internal import POST as int_POST
from storagebin.internal import get_owner as int_get_owner

def DELETE(bin_owner, data_id):
    """Delete a binary object from the datastore
    
    Args:
        bin_owner: the owner Model
        data_id: a numeric identifier for Binary object
    
    Returns:
        content: an object or string for output via HttpResponse or HttpResponseRedirect
        content_type: describes the content aka mimetype for output in header
        status: a HTTP status code
    """
    return int_DELETE(bin_owner, data_id)

def GET(data_id):
    """Get a binary object from the datastore
    
    Args:
        data_id: a numeric identifier for Binary object
    
    Returns:
        content: an object or string for output via HttpResponse or HttpResponseRedirect
        content_type: describes the content aka mimetype for output in header
        status: a HTTP status code
    """
    return int_GET(data_id)

def POST(bin_owner, data_id, uploaded_file):
    """Add/update a binary object to/in the datastore
    
    Args:
        bin_owner: the owner Model
        data_id: a numeric identifier for Binary object
        uploaded_file: an instance of django.http.UploadedFile
    
    Returns:
        content: an object or string for output via HttpResponse or HttpResponseRedirect
        content_type: describes the content aka mimetype for output in header
        status: a HTTP status code
    """
    return int_POST(bin_owner, data_id, uploaded_file)

def get_owner(owner_key):
    """Retrieve the BinOwner object via the owner_key
    
    Args:
        owner_key: string finger print of the user
    
    Returns:
        BinOwner
    """
    return int_get_owner(owner_key)
