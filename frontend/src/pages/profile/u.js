import { useRouter } from 'next/router';
import Link from "next/link";
import {useContext} from "react";
import {AuthContext} from "../../contexts/AuthContext";

const UserProfile = () => {
    const router = useRouter();
    const { user, loading } = useContext(AuthContext)

    if (typeof window !== 'undefined' && !user && !loading)
        router.push('/login');

    return (
        <div className='p-5 bg-light rounded-3'>
            <div className='container-fluid py-3'>
                <h1 className='display-5 fw-bold'>
                    User Profile
                </h1>
                <Link href='/profile/session-history'>
                    <a className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                        Session History
                    </a>
                </Link>
                <Link href='/profile/billing'>
                    <a className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                        Billing
                    </a>
                </Link>
            </div>
        </div>
    );
};

export default UserProfile;

export async function getServerSideProps(context) {
  return {
    props: {
      protected: true
    },
  }
}