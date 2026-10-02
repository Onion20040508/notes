// Page-style switcher: a palette button next to the dark-mode button. The chosen look is stored in
// the reader's browser and applied as <html data-look="...">; the looks themselves are in custom.scss.
// postbuild.py adds this script to every page, plus a tiny inline script that applies the saved look
// before the page is drawn.
(function () {
  var KEY = "site-look"
  var LOOKS = [
    ["", "Default", "inherit"],
    ["notes", "Course notes", '"Source Serif 4", Georgia, serif'],
    ["modern", "Quiet modern", '"IBM Plex Sans", system-ui, sans-serif'],
    ["book", "Printed book", '"EB Garamond", Georgia, serif'],
  ]
  var ICON =
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/>' +
    '<path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/></svg>'

  function current() {
    return document.documentElement.getAttribute("data-look") || ""
  }

  function apply(look) {
    if (look) document.documentElement.setAttribute("data-look", look)
    else document.documentElement.removeAttribute("data-look")
    try {
      if (look) localStorage.setItem(KEY, look)
      else localStorage.removeItem(KEY)
    } catch (e) {}
    document.querySelectorAll(".look-menu [data-look]").forEach(function (b) {
      b.setAttribute("aria-checked", String(b.getAttribute("data-look") === look))
    })
  }

  function mount() {
    // Quartz replaces the page body on every navigation, so the button is added again each time.
    document.querySelectorAll("button.darkmode").forEach(function (dark) {
      var slot = dark.parentElement
      if (!slot || !slot.parentElement || slot.parentElement.querySelector(".look-switch")) return
      var wrap = slot.cloneNode(false) // keeps the toolbar's flex settings
      wrap.classList.add("look-switch")
      var items = LOOKS.map(function (l) {
        return (
          '<button role="menuitemradio" data-look="' + l[0] + '" aria-checked="' + (l[0] === current()) +
          '" style="font-family:' + l[2].replace(/"/g, "&quot;") + '">' + l[1] + "</button>"
        )
      }).join("")
      wrap.innerHTML =
        '<button class="look-button" aria-label="Page style" aria-haspopup="menu" aria-expanded="false">' + ICON + "</button>" +
        '<div class="look-menu" role="menu" aria-label="Page style" hidden>' + items + "</div>"
      slot.parentElement.insertBefore(wrap, slot)
    })
  }

  function closeMenus() {
    document.querySelectorAll(".look-menu").forEach(function (m) { m.hidden = true })
    document.querySelectorAll(".look-button").forEach(function (b) { b.setAttribute("aria-expanded", "false") })
  }

  document.addEventListener("click", function (e) {
    var button = e.target.closest && e.target.closest(".look-button")
    var item = e.target.closest && e.target.closest(".look-menu [data-look]")
    if (button) {
      var menu = button.parentElement.querySelector(".look-menu")
      var open = menu.hidden
      closeMenus()
      menu.hidden = !open
      button.setAttribute("aria-expanded", String(open))
    } else if (item) {
      apply(item.getAttribute("data-look"))
      closeMenus()
    } else if (!(e.target.closest && e.target.closest(".look-menu"))) {
      closeMenus()
    }
  })
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenus()
  })
  document.addEventListener("nav", mount)
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount)
  else mount()
})()
