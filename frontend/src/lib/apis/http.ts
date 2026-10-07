import { PUBLIC_API_BASE_URL } from '$env/static/public';

export async function fetchResource<T>(token: string, url: string): Promise<T> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/${url}`, {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${token}`
		}
	});
	const result = await response.json();
	if (!response.ok) {
		throw { status: response.status, errors: result.detail || 'Something went wrong' };
	}
	return result as T;
}

export async function postResource<T, S>(payload: T, token: string, url: string): Promise<S> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/${url}`, {
		method: 'POST',
		body: JSON.stringify(payload),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${token}`
		}
	});
	const result = await response.json();
	if (!response.ok) {
		throw { status: response.status, errors: result.detail || 'Something went wrong' };
	}
	return result as S; // Cast to the explicit response interface
}

export async function deleteResource(token: string, url: string): Promise<boolean> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/${url}`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${token}`
		}
	});
	if (response.status !== 204) {
		const result = await response.json();
		throw { status: response.status, errors: result.detail };
	}
	return true;
}

export async function updateResource<T, S>(payload: T, token: string, url: string): Promise<S> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/${url}`, {
		method: 'PATCH',
		body: JSON.stringify(payload),
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${token}`
		}
	});
	const result = await response.json();
	if (!response.ok) {
		throw { status: response.status, errors: result.detail || 'Something went wrong' };
	}
	return result as S; // Cast to the explicit response interface
}
