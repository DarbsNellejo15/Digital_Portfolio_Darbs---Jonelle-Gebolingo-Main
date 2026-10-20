$(document).ready(function () {

    $('#menu').click(function () {
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });

    $(window).on('scroll load', function () {
        $('#menu').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        if (window.scrollY > 60) {
            document.querySelector('#scroll-top').classList.add('active');
        } else {
            document.querySelector('#scroll-top').classList.remove('active');
        }

        // scroll spy
        $('section').each(function () {
            let height = $(this).height();
            let offset = $(this).offset().top - 200;
            let top = $(window).scrollTop();
            let id = $(this).attr('id');

            if (top > offset && top < offset + height) {
                $('.navbar ul li a').removeClass('active');
                $('.navbar').find(`[href="#${id}"]`).addClass('active');
            }
        });
    });

    // smooth scrolling
    $('a[href*="#"]').on('click', function (e) {
        if ($(this).attr('href') === '#') return;
        e.preventDefault();
        const target = $($(this).attr('href'));
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top - 60,
            }, 500, 'linear');
        }
    });

    // Contact form handling with feedback banner
    $("#contact-form").submit(function (event) {
        event.preventDefault();
        const submitBtn = $(this).find('button[type="submit"]');
        const originalText = submitBtn.html();
        
        submitBtn.html('Sending... <i class="fas fa-spinner fa-spin"></i>').prop('disabled', true);

        // Simulate sending / success response
        setTimeout(function () {
            submitBtn.html('Message Sent! <i class="fas fa-check"></i>').css('background', '#10b981');
            document.getElementById("contact-form").reset();
            
            setTimeout(function () {
                submitBtn.html(originalText).prop('disabled', false).css('background', '');
            }, 3000);
        }, 800);
    });

});

document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === "visible") {
        document.title = "DARBS | Jonelle Gebolingo Portfolio";
        $("#favicon").attr("href", "/assets/images/favicon.png");
    } else {
        document.title = "Come Back To DARBS Portfolio";
        $("#favicon").attr("href", "/assets/images/favhand.png");
    }
});

// <!-- typed js effect starts -->
if (document.querySelector(".typing-text")) {
    var typed = new Typed(".typing-text", {
        strings: [
            "Information Technology Student",
            "Web Developer",
            "Web Designer",
            "IT Troubleshooting Enthusiast",
            "Future IT Professional"
        ],
        loop: true,
        typeSpeed: 50,
        backSpeed: 25,
        backDelay: 1000,
    });
}
// <!-- typed js effect ends -->

// Global data store for modal access
let certificatesData = [];

async function fetchData(type = "skills") {
    let response;
    if (type === "skills") {
        response = await fetch("/skills.json");
    } else if (type === "projects") {
        response = await fetch("/projects/projects.json");
    } else if (type === "certificates") {
        response = await fetch("/certificates.json");
    }
    const data = await response.json();
    return data;
}

function showSkills(skills) {
    let skillsContainer = document.getElementById("skillsContainer");
    if (!skillsContainer) return;
    let skillHTML = "";
    skills.forEach(skill => {
        const color = skill.color || '#ffe600';
        const glow = skill.glow || 'rgba(255, 230, 0, 0.4)';
        const category = skill.category || 'all';
        const badge = skill.badge || '';

        skillHTML += `
        <div class="bar skill-card" data-category="${category}" style="--skill-color: ${color}; --skill-glow: ${glow};">
            <div class="info">
                <div class="icon-wrap">
                    <i class="${skill.icon}" aria-hidden="true"></i>
                </div>
                <span>${skill.name}</span>
                ${badge ? `<small class="skill-badge">${badge}</small>` : ''}
            </div>
        </div>`;
    });
    skillsContainer.innerHTML = skillHTML;

    setupSkillsFilter();
}

function setupSkillsFilter() {
    $('.skills-filter-container .filter-btn').off('click').on('click', function () {
        $('.skills-filter-container .filter-btn').removeClass('active');
        $(this).addClass('active');
        const filter = $(this).data('filter');

        if (filter === 'all') {
            $('#skillsContainer .skill-card').stop().css('display', 'block').animate({ opacity: 1 }, 200);
        } else {
            $('#skillsContainer .skill-card').each(function () {
                const itemCategory = $(this).data('category');
                if (itemCategory === filter) {
                    $(this).stop().css('display', 'block').animate({ opacity: 1 }, 200);
                } else {
                    $(this).stop().animate({ opacity: 0 }, 150, function () {
                        $(this).css('display', 'none');
                    });
                }
            });
        }
    });
}

function showProjects(projects) {
    let projectsContainer = document.querySelector("#work .box-container");
    if (!projectsContainer) return;
    let projectHTML = "";
    projects.forEach(project => {
        const imagePath = project.image.startsWith('/') 
            ? project.image 
            : `/assets/images/projects/${project.image}.png`;

        const techBadges = project.technologies 
            ? project.technologies.map(t => `<span class="tech-badge">${t}</span>`).join('') 
            : '';

        const viewUrl = project.links.view && project.links.view !== '#' 
            ? project.links.view 
            : project.links.code;

        projectHTML += `
        <div class="box tilt">
            <img draggable="false" src="${imagePath}" alt="${project.name}" />
            <div class="content">
                <div class="tag">
                    <h3>${project.name}</h3>
                    <a href="${viewUrl}" class="project-view-link" target="_blank" rel="noopener noreferrer" title="View ${project.name}"><i class="fas fa-eye"></i> View</a>
                </div>
                <div class="desc">
                    <p>${project.desc}</p>
                    ${techBadges ? `<div style="margin-top:0.8rem;">${techBadges}</div>` : ''}
                    <div class="btns">
                        <a href="${viewUrl}" class="btn" target="_blank" rel="noopener noreferrer"><i class="fas fa-eye"></i> View Project</a>
                        <a href="${project.links.code}" class="btn" target="_blank" rel="noopener noreferrer">Code <i class="fas fa-code"></i></a>
                    </div>
                </div>
            </div>
        </div>`;
    });
    projectsContainer.innerHTML = projectHTML;

    // <!-- tilt js effect starts -->
    if (typeof VanillaTilt !== "undefined") {
        VanillaTilt.init(document.querySelectorAll(".tilt"), {
            max: 15,
        });
    }

    /* ===== SCROLL REVEAL ANIMATION ===== */
    if (typeof ScrollReveal !== "undefined") {
        const srtop = ScrollReveal({
            origin: 'top',
            distance: '80px',
            duration: 1000,
            reset: false
        });
        srtop.reveal('.work .box', { interval: 200 });
    }
}

function showCertificates(certificates) {
    certificatesData = certificates;
    let certContainer = document.getElementById("certificatesContainer");
    if (!certContainer) return;
    let certHTML = "";
    certificates.forEach((cert, idx) => {
        const thumbnail = cert.image
            ? `<img src="${cert.image}" alt="${cert.title}" draggable="false" />`
            : `<div class="cert-pdf-thumb"><i class="fas fa-file-pdf"></i><span>PDF Certificate</span></div>`;
        const year = cert.year
            ? `<div class="cert-year"><i class="fas fa-calendar-alt"></i> ${cert.year}</div>`
            : "";
        const profileLink = cert.profileUrl
            ? `<a class="cert-btn cert-profile-link" href="${cert.profileUrl}" target="_blank" rel="noopener noreferrer">
                    <i class="fas fa-external-link-alt"></i> View NetAcad Profile
                </a>`
            : "";
        certHTML += `
        <div class="cert-card tilt" id="cert-card-${cert.id}">
            <div class="cert-thumb">
                ${thumbnail}
                <span class="cert-badge"><i class="fas fa-award"></i> Verified</span>
            </div>
            <div class="cert-body">
                <div>
                    <h3>${cert.title}</h3>
                    <div class="cert-issuer">
                        <i class="fas fa-building"></i> ${cert.issuer}
                    </div>
                    ${year}
                    <p class="cert-desc">${cert.description}</p>
                </div>
                <div class="cert-actions">
                    <button class="cert-btn" type="button" onclick="openCertModal(${idx})">
                        <i class="fas fa-eye"></i> View Certificate
                    </button>
                    ${profileLink}
                </div>
            </div>
        </div>`;
    });
    certContainer.innerHTML = certHTML;

    if (typeof VanillaTilt !== "undefined") {
        VanillaTilt.init(document.querySelectorAll("#certificates .tilt"), {
            max: 10,
        });
    }
}

// Certificate Modal Functions
window.openCertModal = function (index) {
    const cert = certificatesData[index];
    if (!cert) return;

    const modal = document.getElementById("certModal");
    const modalImg = document.getElementById("modalCertImg");
    const modalTitle = document.getElementById("modalCertTitle");
    const modalIssuer = document.getElementById("modalCertIssuer");
    const modalYear = document.getElementById("modalCertYear");
    const modalDesc = document.getElementById("modalCertDesc");
    const modalCredential = document.getElementById("modalCertCredential");

    if (modalImg) modalImg.src = cert.image;
    if (modalTitle) modalTitle.textContent = cert.title;
    if (modalIssuer) modalIssuer.innerHTML = `<i class="fas fa-building"></i> Issuing Body: <strong>${cert.issuer}</strong>`;
    if (modalYear) {
        modalYear.innerHTML = cert.year
            ? `<i class="fas fa-calendar-check"></i> Year Issued: <strong>${cert.year}</strong>`
            : "";
    }
    if (modalDesc) modalDesc.textContent = cert.description;
    if (modalCredential) modalCredential.innerHTML = `Credential ID: <span>${cert.credentialId}</span>`;

    if (modal) {
        modal.classList.add("open");
        document.body.style.overflow = "hidden";
    }
};

window.closeCertModal = function () {
    const modal = document.getElementById("certModal");
    if (modal) {
        modal.classList.remove("open");
        document.body.style.overflow = "";
    }
};

// Close modal on escape key
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
        window.closeCertModal();
    }
});

// Close modal on backdrop click
$(document).on("click", "#certModal", function (e) {
    if (e.target.id === "certModal") {
        window.closeCertModal();
    }
});

fetchData("skills").then(data => {
    showSkills(data);
}).catch(err => console.error("Error loading skills:", err));

fetchData("projects").then(data => {
    showProjects(data);
}).catch(err => console.error("Error loading projects:", err));

fetchData("certificates").then(data => {
    showCertificates(data);
}).catch(err => console.error("Error loading certificates:", err));

// <!-- tilt js effect starts -->
if (typeof VanillaTilt !== "undefined") {
    VanillaTilt.init(document.querySelectorAll(".tilt"), {
        max: 15,
    });
}

/* ===== SCROLL REVEAL ANIMATION ===== */
if (typeof ScrollReveal !== "undefined") {
    const srtop = ScrollReveal({
        origin: 'top',
        distance: '80px',
        duration: 1000,
        reset: false
    });

    /* SCROLL HOME */
    srtop.reveal('.home .image', { delay: 200 });
    srtop.reveal('.home .content h2', { delay: 300 });
    srtop.reveal('.home .content p', { delay: 300 });
    srtop.reveal('.home .content .btn', { delay: 300 });
    srtop.reveal('.home .social-icons li', { interval: 200 });

    /* SCROLL ABOUT */
    srtop.reveal('.about .content h3', { delay: 200 });
    srtop.reveal('.about .content .tag', { delay: 200 });
    srtop.reveal('.about .content p', { delay: 200 });
    srtop.reveal('.about .content .box-container', { delay: 200 });

    /* SCROLL SKILLS */
    srtop.reveal('.skills .container', { interval: 200 });

    /* SCROLL EDUCATION */
    srtop.reveal('.education .box', { interval: 200 });

    /* SCROLL CERTIFICATES */
    srtop.reveal('.certificates .cert-card', { interval: 200 });

    /* SCROLL EXPERIENCE */
    srtop.reveal('.experience .timeline', { delay: 400 });
    srtop.reveal('.experience .timeline .container', { interval: 300 });

    /* SCROLL CONTACT */
    srtop.reveal('.contact .container', { delay: 300 });
}

// Resume download toast notification
$(document).on('click', 'a[download*="Resume"], a[download*="resume"], .btn-resume, #aboutResumeBtn', function() {
    showToast("Starting download for Jonelle Gebolingo's Resume...");
});

function showToast(message) {
    let toast = document.getElementById('portfolioToast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'portfolioToast';
        toast.className = 'portfolio-toast';
        document.body.appendChild(toast);
    }
    toast.innerHTML = `<i class="fas fa-file-pdf"></i> <span>${message}</span>`;
    toast.classList.add('show');
    clearTimeout(window.toastTimer);
    window.toastTimer = setTimeout(() => {
        toast.classList.remove('show');
    }, 3500);
}
