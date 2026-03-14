function changeView(view) {
    const carImage = document.getElementById('main-car');
    
    const views = {
        'front': 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800',
        'back': 'https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?w=800',
        'side': 'https://images.unsplash.com/photo-1580273916550-e323be2ae537?w=800',
        'interior': 'https://images.unsplash.com/photo-1617814076367-b759c7d6273c?w=800'
    };

    if (views[view]) {
        carImage.style.opacity = 0; 
        setTimeout(() => {
            carImage.src = views[view];
            carImage.style.opacity = 1;
        }, 300);
    }
}