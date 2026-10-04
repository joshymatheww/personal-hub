import { getContext, setContext } from 'svelte';

import type { Account, FinanceMeataData } from '$lib/types/finance';
import { createQuery } from '@tanstack/svelte-query';
import { fetchResource } from '$lib/apis/http';
import { authStore } from './auth-store.svelte';

export class FinanceStore {
	// Getting metadata
	meataDataQuery = createQuery<FinanceMeataData>(() => ({
		queryKey: ['finance-metadata'],
		queryFn: () => fetchResource<FinanceMeataData>(authStore.token || '', 'finance/metadata'),
		enabled: !!authStore.token,
		staleTime: 1000 * 60 * 5
	}));
	// Getting all the accounts
	accountsQuery = createQuery<Account[]>(() => ({
		queryKey: ['finance-accounts'],
		queryFn: () => fetchResource<Account[]>(authStore.token || '', 'finance/accounts'),
		enabled: !!authStore.token,
		staleTime: 1000 * 60 * 5
	}));

	getMeataData() {
		return this.meataDataQuery;
	}
	getAllAccounts() {
		return this.accountsQuery;
	}

	accountTypes = $derived.by(() => {
		const query = this.meataDataQuery;
		return query.data ? query.data.account_types : [];
	});
}

const FINANCE_STATE_KEY = Symbol('FINANCE_STATE');

export function setFinanceState() {
	return setContext(FINANCE_STATE_KEY, new FinanceStore());
}

export function getFinanceState() {
	return getContext<ReturnType<typeof setFinanceState>>(FINANCE_STATE_KEY);
}
