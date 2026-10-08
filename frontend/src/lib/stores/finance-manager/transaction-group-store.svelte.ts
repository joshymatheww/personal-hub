import { getContext, setContext } from 'svelte';

import type { TransactionGroup } from '$lib/types/finance';
import { createQuery } from '@tanstack/svelte-query';
import { fetchResource } from '$lib/apis/http';
import { authStore } from '../auth-store.svelte';

export class TransactionGroupStore {
	// Getting all the transaction groups
	transactionGroupQuery = createQuery<TransactionGroup[]>(() => ({
		queryKey: ['finance-transaction-group'],
		queryFn: () =>
			fetchResource<TransactionGroup[]>(authStore.token || '', 'finance/transaction-group'),
		enabled: !!authStore.token,
		staleTime: 1000 * 60 * 5
	}));

	getAllTransactionGroups() {
		return this.transactionGroupQuery;
	}
}

const TRANSACTION_GROUP_STATE_KEY = Symbol('TRANSCTION_GROUP_STATE');

export function setTransactionGroupState() {
	return setContext(TRANSACTION_GROUP_STATE_KEY, new TransactionGroupStore());
}

export function getTransactionGroupState() {
	return getContext<ReturnType<typeof setTransactionGroupState>>(TRANSACTION_GROUP_STATE_KEY);
}
