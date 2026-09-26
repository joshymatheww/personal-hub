<script lang="ts">
	import Dumbell from '../icons/Dumbell.svelte';
</script>

<div
	class="brand-panel relative hidden flex-col justify-between bg-rail p-10 text-white lg:flex xl:p-14"
>
	<div class="flex items-center gap-2">
		<span class="grid h-9 w-9 place-items-center rounded-md bg-white/10">
			<Dumbell />
		</span>
		<span class="font-display text-lg font-semibold">Workout log</span>
	</div>

	<div class="max-w-sm">
		<p class="font-display text-3xl leading-tight font-bold xl:text-4xl">
			Know exactly what to train today.
		</p>
		<p class="mt-4 text-white/60">
			Every session you log updates the recovery ladder, so the next workout picks itself — no more
			guessing if it's leg day.
		</p>
	</div>

	<p class="text-sm text-white/40">© 2026 Workout log</p>
</div>
