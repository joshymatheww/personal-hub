import { fetchResource } from "$lib/apis/http";
import type { Transaction } from "$lib/types/finance";
import { createQuery } from "@tanstack/svelte-query";
import { authStore } from "../auth-store.svelte";
import { getContext, setContext } from "svelte";

export class TransactionStore {
	transactionsQuery = createQuery<Transaction[]>(() => ({
		queryKey: ['finance-transactions'],
		queryFn: () => fetchResource<Transaction[]>(authStore.token || '', 'finance/transactions'),
		enabled: !!authStore.token,
		staleTime: 1000 * 60 * 5
	}));

	getAllTransactions() {
		return this.transactionsQuery
	}
}

const TRANSACTION_STATE_KEY = Symbol('TRANSACTIONS_STATE');

export function setTransactionState() {
	return setContext(TRANSACTION_STATE_KEY, new TransactionStore());
}

export function getTransactionState() {
	return getContext<ReturnType<typeof setTransactionState>>(TRANSACTION_STATE_KEY);
}
