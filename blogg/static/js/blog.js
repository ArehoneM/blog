function togglePost(id) {
    const preview = document.getElementById('preview-' + id);
    const full = document.getElementById('full-' + id);
    
    if (preview.style.display === 'none') {
        preview.style.display = 'block';
        full.style.display = 'none';
    } else {
        preview.style.display = 'none';
        full.style.display = 'block';
    }
}
