import { PUBLIC_API_BASE_URL } from '$env/static/public';
import type { TokenResponse, UserProfile } from '$lib/types/auth';

export async function getToken(email: string, password: string): Promise<TokenResponse> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/token`, {
		method: 'POST',
		body: JSON.stringify({ email, password }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	const result = await response.json();
	if (!response.ok) {
		throw { status: response.status, errors: result.detail || 'Something went wrong' };
	}
	return result as TokenResponse; // Cast to the explicit response interface
}

export async function getCurrentuser(token: string): Promise<UserProfile> {
	const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/me`, {
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
	return result as UserProfile;
}
