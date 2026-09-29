// Theme
(function () {
  const saved = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
})();

function toggleTheme() {
  const now = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', now);
  localStorage.setItem('theme', now);
  const btn = document.getElementById('themeBtn');
  if (btn) btn.textContent = now === 'dark' ? '☀️' : '🌙';
}

function isLoggedIn() {
  return !!localStorage.getItem('user_id');
}

function logout() {
  localStorage.removeItem('user_id');
  localStorage.removeItem('user_name');
  window.location.href = 'index.html';
}

function renderNav() {
  const nav = document.getElementById('nav');
  if (!nav) return;

  const theme = document.documentElement.getAttribute('data-theme');
  const themeIcon = theme === 'dark' ? '☀️' : '🌙';

  let html = '<a href="index.html">Home</a><a href="questions.html">Practice</a>';
  html += `<button class="icon-btn" id="themeBtn" onclick="toggleTheme()">${themeIcon}</button>`;

  if (isLoggedIn()) {
    const name = localStorage.getItem('user_name') || 'User';
    const initial = name.charAt(0).toUpperCase();
    html += `
      <div class="profile">
        <button class="avatar" onclick="toggleDropdown(event)">${initial}</button>
        <div class="dropdown" id="profileMenu">
          <div class="who">Hi, ${name}</div>
          <button onclick="logout()">Logout</button>
        </div>
      </div>`;
  } else {
    html += '<a href="login.html">Login</a><a href="signup.html">Sign Up</a>';
  }
  nav.innerHTML = html;
}

function toggleDropdown(e) {
  e.stopPropagation();
  document.getElementById('profileMenu').classList.toggle('open');
}

document.addEventListener('click', () => {
  const m = document.getElementById('profileMenu');
  if (m) m.classList.remove('open');
});

document.addEventListener('DOMContentLoaded', renderNav);