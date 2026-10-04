<script>
	import { page } from '$app/state';
	import AppIcon from '../icons/AppIcon.svelte';
	import FiananceManager from '../icons/FiananceManager.svelte';
	import WorkoutsManager from '../icons/WorkoutsManager.svelte';
</script>

<aside
	class="fixed inset-y-0 left-0 z-30 hidden w-16 flex-col items-center gap-1 bg-rail py-4 lg:flex"
>
	<a
		href="/app"
		class="mb-4 grid h-10 w-10 place-items-center rounded-md text-white/55 hover:bg-white/10 hover:text-white"
		class:is_active={true}
		aria-label="Workout log home"
	>
		<AppIcon />
	</a>
	<div class="group relative inline-block">
		<a
			href="/app/finance-manager"
			class="rail-link relative grid h-11 w-11 place-items-center rounded-md text-white/55 hover:bg-white/10 hover:text-white"
			class:is_active={page.url.pathname.indexOf('/app/finance-manager') >= 0}
			aria-label="Dashboard"
		>
			<span
				class="rail-mark absolute left-0 h-6 w-0.5 -translate-x-2 rounded-full bg-white opacity-0"
			></span>
			<FiananceManager />
		</a>
		<div
			class="pointer-events-none absolute top-1/2 left-full z-20 ml-3 -translate-y-1/2 scale-75 opacity-0 transition-all duration-200 ease-out group-hover:scale-100 group-hover:opacity-100"
		>
			<!-- Tooltip Content Box -->
			<div class="rounded bg-gray-900 px-3 py-1.5 text-xs whitespace-nowrap text-white shadow-xl">
				Finance Manager
			</div>
			<!-- Tooltip Arrow/Triangle: Moved to the left side of the tooltip box -->
			<div
				class="absolute top-1/2 right-full h-2.5 w-2.5 translate-x-1/2 -translate-y-1/2 rotate-45 bg-gray-900"
			></div>
		</div>
	</div>
	<div class="group relative inline-block">
		<a
			href="/app/workouts-manager"
			class="rail-link relative grid h-11 w-11 place-items-center rounded-md text-white/55 hover:bg-white/10 hover:text-white"
			class:is_active={page.url.pathname.indexOf('/app/workouts-manager') >= 0}
			aria-label="Sessions"
		>
			<span
				class="rail-mark absolute left-0 h-6 w-0.5 -translate-x-2 rounded-full bg-white opacity-0"
			></span>
			<WorkoutsManager />
		</a>
		<div
			class="pointer-events-none absolute top-1/2 left-full z-20 ml-3 -translate-y-1/2 scale-75 opacity-0 transition-all duration-200 ease-out group-hover:scale-100 group-hover:opacity-100"
		>
			<!-- Tooltip Content Box -->
			<div class="rounded bg-gray-900 px-3 py-1.5 text-xs whitespace-nowrap text-white shadow-xl">
				Workouts Manager
			</div>
			<!-- Tooltip Arrow/Triangle: Moved to the left side of the tooltip box -->
			<div
				class="absolute top-1/2 right-full h-2.5 w-2.5 translate-x-1/2 -translate-y-1/2 rotate-45 bg-gray-900"
			></div>
		</div>
	</div>
</aside>
