//trigger => data => screen

import "./style.css";

const username = document.querySelector("#searchInput");
const button = document.querySelector("#searchBtn");
const view = document.querySelector("#profileContainer");

button.addEventListener("click", async () => {
  if (!username.value.trim()) {
    view.innerHTML = `<p class="text-yellow-300 mt-4 font-bold">Please enter a username</p>`;
    return;
  }

  const User = await fetch(
    `https://api.github.com/users/${username.value.trim()}`,
  );

  //how to display inside div? hmm what have i done last time?
  if (!User.ok) {
    view.innerHTML = `<p class="text-red-300 mt-4 font-bold">User not Found</p>`;
    return;
  }

  const data = await User.json(); // important hai yaar mat chhod ese...

  //below code are by ai easy lekin tailwind pe abhi hath tight hai todha..
  view.innerHTML = `
    <div class="mt-6 flex flex-col items-center bg-emerald-800 p-6 rounded-xl shadow-lg text-white">
      <img src="${data.avatar_url}" alt="Avatar" class="w-24 h-24 rounded-full border-4 border-white mb-3" />
      <h2 class="text-xl font-bold">${data.name || data.login}</h2>
      <p class="text-emerald-200 text-sm">@${data.login}</p>
      <p class="mt-2 text-center text-sm">${data.bio || "No bio available"}</p>
      
      <div class="flex gap-4 mt-4 bg-emerald-900 px-4 py-2 rounded-lg text-sm">
        <span><strong>Repos:</strong> ${data.public_repos}</span>
        <span><strong>Followers:</strong> ${data.followers}</span>
      </div>
    </div>
  `;
});
