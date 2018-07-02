import time


def generate_current_timestamp():
    return time.strftime("%Y%m%d_%H%M%S")

def generate_short_timestamp():
    return time.strftime("%H%M%S")

def generate_download_button(filename, title):
    url = 'downloads/'+filename
    return '<a class="btn btn-success" href="'+url+'" target="_blank">'+title+'</a>'

def generate_share_link(root_url, filename):
    url = 'downloads/'+filename
    share_url = root_url+url
    content = '<div class="input-group">'
    content += '    <input id="share_url" class="form-control py-2" type="text" readonly value='+share_url+'>'
    content += '    <span class="input-group-append">'
    content += '        <button id="share_url_copy_btn" class="btn btn-secondary" type="button" data-toggle="popover"'
    content += 'data-trigger="focus" title="Copy URL to clipboard" data-content="Copied to clipboard">'
    content += '            <i class="far fa-copy"></i>'
    content += '        </button>'
    content += '    </span>'
    content += '</div>'
    return content

def generate_card_body(root_url, filename, title, success=True):
    if success == True:
        header_message = "Conversion successful"
        content = ''
        content+='<div class="card-header">'
        content+= '<h4>'+header_message+'</h4>'
        content+='</div>'
        content+='<div class="card-body text-center">'
        content+=    generate_download_button(filename, title)
        content+='</div>'
        content+='<div class="card-footer">'
        content+=    generate_share_link(root_url, filename)
        content+='</div>'
        return content    
