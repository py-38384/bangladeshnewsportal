const slider = document.querySelector('.slider')
const carousel = document.querySelector('.carousel')

const prev = document.querySelector('.controls .prev')
const next = document.querySelector('.controls .next')
let direction = -1

const sliding_proportion = '20%' //  sliding_proportion = 100/number_of_slide


prev.addEventListener('click',(e)=>{
    if(direction === 1){
        slider.style.transform = `translateX(${sliding_proportion})`
    }else{
        carousel.style.justifyContent = 'flex-end'
        slider.appendChild(slider.firstElementChild)
        slider.style.transform = `translateX(${sliding_proportion})`
        direction = 1
    }
    setTimeout(()=>{
        slider.style.transition = 'none'
        slider.prepend(slider.lastElementChild)
        slider.style.transform = "translateX(0)"
        setTimeout(()=>{
            slider.style.transition = '0.3s'
        },100)
    },300)
})

next.addEventListener('click',(e)=>{
    if(direction === -1){
        slider.style.transform = `translateX(-${sliding_proportion})`
    }else{
        carousel.style.justifyContent = 'flex-start'
        slider.prepend(slider.lastElementChild)
        slider.style.transform = `translateX(-${sliding_proportion})`
        direction = -1
    }
    setTimeout(()=>{
        slider.style.transition = 'none'
        slider.appendChild(slider.firstElementChild)
        slider.style.transform = "translateX(0)"
        setTimeout(()=>{
            slider.style.transition = '0.3s'
        },100)
    },300)
})