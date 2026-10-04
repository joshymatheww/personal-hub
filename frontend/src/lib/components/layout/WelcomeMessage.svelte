<script lang="ts">
	import AppIcon from '../icons/AppIcon.svelte';
</script>

<div
	class="brand-panel relative hidden flex-col justify-between bg-rail p-10 text-white lg:flex xl:p-14"
>
	<div class="flex items-center gap-2">
		<span class="grid h-9 w-9 place-items-center rounded-md bg-white/10">
			<AppIcon />
		</span>
		<span class="font-display text-lg font-semibold">Personal Hub</span>
	</div>

	<div class="max-w-sm">
		<p class="font-display text-3xl leading-tight font-bold xl:text-4xl">
			Health & Wealth, perfectly tracked.
		</p>
		<p class="mt-4 text-white/60">
			Every training session updates your recovery status, while every transaction secures your cash
			flow. One unified dashboard to optimize your health and your wealth—zero guesswork required.
		</p>
	</div>

	<p class="text-sm text-white/40">© {new Date().getFullYear()} Personal hub</p>
</div>
